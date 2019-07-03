#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `quipclient` classes."""


from unittest import mock
import pytest

from quare.quip_classes import QuipFolder, QuipThread, QuipMessage


@pytest.fixture
def folder(starred_folder):
    """Return an instance of QuipFolder"""
    return QuipFolder(**starred_folder)


@pytest.fixture
def document(document_thread):
    """Return an instance of QuipFolder"""
    return QuipThread(**document_thread)


def test_folder__folder_init(starred_folder, folder):
    """Assert the Quip Folder instance variables are correct."""
    assert folder.meta.id == starred_folder["folder"]["id"]
    assert len(folder.children) == 2
    assert len(folder.member_ids) == 2


def test_folder__get_child_threads(folder):
    assert len(folder.children) == 2
    assert folder.child_threads == ["ULJAAAkvOHx"]


def test_folder__get_child_folders(folder):
    assert len(folder.children) == 2
    assert folder.child_folders == ["LEMAOAQNQwb"]


def test_thread__thread_init(document_thread, document):
    """Assert the QuipThread instance variables are correct."""
    assert document.meta.id == document_thread["thread"]["id"]
    assert document.user_ids == ["ffHAEAEIfch"]


@mock.patch("quare.quip.QuipClient.get_thread")
def test_thread__get_thread(get_thread, document_thread):
    get_thread.return_value = document_thread
    thread = QuipThread.get_thread("fakeToken", "FakeID")
    assert thread.id == document_thread["thread"]["id"]


@mock.patch("quare.quip.QuipClient.get_thread")
@mock.patch("quare.quip.QuipClient.get_messages")
def test_thread__get_messages(get_msg, get_thread, document_thread, thread_messages):
    get_thread.return_value = document_thread
    get_msg.return_value = thread_messages
    thread = QuipThread.get_thread("fakeToken", "FakeID")
    msgs = thread.get_messages("token")
    assert len(msgs) == len(thread_messages)
    assert thread.id == document_thread["thread"]["id"]


def test_message__from_dict(thread_messages):
    msg_dict = thread_messages[0]
    msg_dict["undocumented_key"] = "foo"
    msg = QuipMessage.from_dict(msg_dict)
    # No TypeError is a pass
    assert msg.id == "fYbADAn7ufP"
