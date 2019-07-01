#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `quare` cli interface."""

import json
import os
from unittest import mock

from click.testing import CliRunner

from quare import cli, quare, ui_messages
from quare.quip_classes import QuipThread


def test_command_line_entry():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--version  Show the version and exit." in help_result.output


@mock.patch("keyring.get_password", return_value=None)
def test_whoami__raises_token_error(key):
    """Verify whoami command json output"""
    quare.TOKEN_ENV_VAR = "IQPOEWACKN"
    runner = CliRunner()
    result = runner.invoke(cli.whoami)
    output = str(result.exception)
    assert result.exit_code == 1
    assert ui_messages.TOKEN_ERROR_MESSAGE == output


@mock.patch("quare.quip.QuipClient.get_authenticated_user")
def test_whoami__table_output(get_user_info, current_user):
    """Verify whoami command output"""
    current_user_table = """\x1b(0l\x1b(BDefault\x1b(0qqqqqqqwqqqqqqqqqqqqqqqqqqqqqqqqqqk\x1b(B
\x1b(0x\x1b(B Name         \x1b(0x\x1b(B Humphrey Appleby         \x1b(0x\x1b(B
\x1b(0tqqqqqqqqqqqqqqnqqqqqqqqqqqqqqqqqqqqqqqqqqu\x1b(B
\x1b(0x\x1b(B Email(s)     \x1b(0x\x1b(B testerino@mailinator.com \x1b(0x\x1b(B
\x1b(0tqqqqqqqqqqqqqqnqqqqqqqqqqqqqqqqqqqqqqqqqqu\x1b(B
\x1b(0x\x1b(B Quip User ID \x1b(0x\x1b(B kcEdRH43BMb7             \x1b(0x\x1b(B
\x1b(0mqqqqqqqqqqqqqqvqqqqqqqqqqqqqqqqqqqqqqqqqqj\x1b(B
"""
    os.environ[quare.TOKEN_ENV_VAR] = "fake token"
    get_user_info.return_value = current_user
    runner = CliRunner()
    result = runner.invoke(cli.whoami)
    assert result.exit_code == 0
    assert current_user_table == result.output


@mock.patch("quare.quip.QuipClient.get_authenticated_user")
def test_whoami__json(get_user_info, current_user):
    """Verify whoami command json output"""
    os.environ[quare.TOKEN_ENV_VAR] = "fake token"
    get_user_info.return_value = current_user
    runner = CliRunner()
    result = runner.invoke(cli.whoami, ["--json"])
    assert result.exit_code == 0
    assert json.dumps(current_user) + "\n" == result.output


@mock.patch("quare.cli.set_user_token")
def test_auth__sets_token(set_token):
    runner = CliRunner()
    result = runner.invoke(cli.auth, ["--alias", "foo"], input="barbarbarbar")
    assert result.exit_code == 0
    set_token.assert_called_with("foo", "barbarbarbar")


def test_auth__fails_without_alias():
    runner = CliRunner()
    result = runner.invoke(cli.auth, "foo", input="barbarbarbar")
    # Error code 2 is missing keyword
    assert result.exit_code == 2


def test_doc():
    """Test flags"""
    runner = CliRunner()
    help_result = runner.invoke(cli.message, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output


@mock.patch("quare.quip.QuipClient.edit_document")
@mock.patch("quare.quare.get_user_token")
def test_doc_append__file(get_user, edit_doc, tmpdir, markdown_content):
    """Verify file access"""
    os.environ[quare.TOKEN_ENV_VAR] = "fake token"
    get_user.return_value = ("alias", "Fake token")
    tmppath = tmpdir.join("foo.txt")
    tmppath.write(markdown_content)
    runner = CliRunner()
    result = runner.invoke(cli.doc_append, ["-i", "fake_id", "--file", tmppath])
    assert result.exit_code == 0
    edit_doc.assert_called_once()
    edit_doc.assert_called_with("fake_id", f"\n{markdown_content}\n", format="markdown")


@mock.patch("quare.quip.QuipClient.edit_document")
@mock.patch("quare.quare.get_user_token")
def test_doc_append__content(get_user, edit_doc, markdown_content):
    """Verify file access"""
    os.environ[quare.TOKEN_ENV_VAR] = "fake token"
    get_user.return_value = ("alias", "Fake token")
    runner = CliRunner()
    result = runner.invoke(
        cli.doc_append, ["-i", "fake_id", "--content", markdown_content]
    )
    assert result.exit_code == 0
    edit_doc.assert_called_once()
    edit_doc.assert_called_with("fake_id", f"\n{markdown_content}\n", format="markdown")


@mock.patch("quare.quip.QuipClient.edit_document")
@mock.patch("quare.quare.get_user_token")
def test_doc_append__empty_content(get_user, edit_doc, markdown_content):
    """Verify file access"""
    os.environ[quare.TOKEN_ENV_VAR] = "fake token"
    get_user.return_value = ("alias", "Fake token")
    runner = CliRunner()
    result = runner.invoke(cli.doc_append, ["-i", "fake_id"], catch_exceptions=False)
    assert result.exit_code == 2
    assert 'Error: You must pass either "--content" or "--file".' in result.output
    edit_doc.assert_not_called()


def test_msg():
    """Test flags"""
    runner = CliRunner()
    help_result = runner.invoke(cli.message, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output


def test_msg_get__room_required():
    runner = CliRunner()
    result = runner.invoke(cli.msg_get, ["--last", 100])
    assert result.exit_code == 2


@mock.patch("quare.cli.get_user_token")
@mock.patch("quare.quip_classes.QuipThread.get_messages")
@mock.patch("quare.quip_classes.QuipThread.get_thread")
def test_msg_get__last_n_messages(
    get_thread, get_msg, get_user, thread_messages, document_thread
):
    os.environ[quare.TOKEN_ENV_VAR] = "fake token"
    get_user.return_value = ("alias", "Fake token")
    get_thread.return_value = QuipThread(**document_thread)
    get_msg.return_value = thread_messages
    runner = CliRunner()
    result = runner.invoke(cli.msg_get, args=["--last", 2, "--room", "roomId"])
    get_thread.assert_called_once()
    get_msg.assert_called_once()
    get_user.assert_called_once()
    assert (
        result.output
        == "[Sun Jun  9 18:12:05 2019 | @James Estevez] Even more recent\n[Sun Mar 31 19:43:34 2019 | @James Estevez] Here is a more recent message\n"
    )
