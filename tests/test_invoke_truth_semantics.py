from canon.api import invoke as invoke_module
from canon.api.commands import Command


def test_handlerless_command_does_not_report_success(monkeypatch):
    command = Command(
        name="unwired-test-command",
        node="HERMES",
        description="fixture",
        category="diagnostic",
        handler=None,
    )

    monkeypatch.setattr(invoke_module, "get_command", lambda name: command)
    monkeypatch.setattr(invoke_module, "list_commands", lambda: [command])

    result = invoke_module.invoke(command.name)

    assert result.success is False
    assert result.node == "HERMES"
    assert result.output is None
    assert result.error == "HANDLER_NOT_WIRED"
