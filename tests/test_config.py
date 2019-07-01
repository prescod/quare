#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `quare` cli interface."""

from unittest import mock

import pytest

from quare.config import quareConfig
from quare.exceptions import ConfigNotFoundError


@pytest.fixture
def config_yaml():
    """Pytest fixture returning a mock configuration YAML file."""
    return """\
defaults:
  chats:
    - alias: Project X
      id: XGXXMseqRKS
      name: Aphrodite Devs
    - alias: MyTeamChat
      id: pSYnMtxtAhy
      name: Pizza Team Chat
      alert: keywords
      keywords:
        - Anchovies
        - Sardines
  documents:
    - alias: Project X Spike
      id: dp2CcxcmiCq
      alert: always\n"""


@pytest.fixture
def parsed_yaml():
    return {
        "defaults": {
            "chats": [
                {"alias": "Project X", "id": "XGXXMseqRKS", "name": "Aphrodite Devs"},
                {
                    "alias": "MyTeamChat",
                    "id": "pSYnMtxtAhy",
                    "name": "Pizza Team Chat",
                    "alert": "keywords",
                    "keywords": ["Anchovies", "Sardines"],
                },
            ],
            "documents": [
                {"alias": "Project X Spike", "id": "dp2CcxcmiCq", "alert": "always"}
            ],
        }
    }


def test_config__init_sets_default_file(tmpdir, config_yaml):
    """Verify that the default path is used when none is given."""
    conf_dir = tmpdir.mkdir("test").join("test.yaml")
    conf_dir.write(config_yaml)
    quareConfig.DEFAULT_CONFIG_FILENAME = conf_dir
    config = quareConfig()
    assert config.config_path == quareConfig.DEFAULT_CONFIG_FILENAME


def test_config__init_sets_throws_exception(tmpdir, config_yaml):
    """Verify that an exception is thrown when the config is not readable."""
    quareConfig.DEFAULT_CONFIG_FILENAME = "a87rhamnntoc7g"
    with pytest.raises(ConfigNotFoundError):
        quareConfig()


@mock.patch("os.path.isfile", return_val=[True, True])
def test_config__init_loads_config(isfile, config_yaml, parsed_yaml):
    """Verify that the config is read, and values match the fixture."""
    with mock.patch("builtins.open", mock.mock_open(read_data=config_yaml)):
        config = quareConfig()
        assert config.config_path == quareConfig.DEFAULT_CONFIG_FILENAME
        assert config.raw_config == parsed_yaml


def test_config__default_doc_list(tmpdir, config_yaml, parsed_yaml):
    """Verify that the config is read, and values match the fixture."""
    conf_dir = tmpdir.join("test.yaml")
    conf_dir.write(config_yaml)
    config = quareConfig(conf_dir)
    assert config.default_docs == parsed_yaml["defaults"]["documents"]


def test_config__default_chat_list(tmpdir, config_yaml, parsed_yaml):
    """Verify that the config is read, and values match the fixture."""
    conf_dir = tmpdir.join("test.yaml")
    conf_dir.write(config_yaml)
    config = quareConfig(conf_dir)
    assert config.default_chats == parsed_yaml["defaults"]["chats"]
