from __future__ import annotations

import sys

import mph


def main() -> int:
    print(f"python={sys.version.split()[0]}")
    print(f"mph={getattr(mph, '__version__', 'unknown')}")

    # Stand-alone is the fastest local mode on Windows when available.
    mph.option("session", "stand-alone")
    client = mph.start(cores=1)
    print(f"client={client!r}")

    try:
        modules = client.modules()
        print("modules:")
        for module in modules:
            print(f"- {module}")
    except Exception as exc:  # noqa: BLE001 - smoke test should report raw COMSOL issues.
        print(f"modules_error={type(exc).__name__}: {exc}")

    try:
        model = client.create("smoke_empty_model")
        print(f"created_model={model.name()}")
        print(f"model_version={model.version()}")
        client.remove(model)
    except Exception as exc:  # noqa: BLE001 - keep this diagnostic broad.
        print(f"create_error={type(exc).__name__}: {exc}")
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
