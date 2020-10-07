import env
import importlib


def pytest_configure(config):
    try:
        env_testing = importlib.__import__('env_testing')
        variables_env_testing = set(
            filter(lambda x: not x.startswith('__'), dir(env_testing))
        )

        for key in variables_env_testing:
            setattr(env, key, getattr(env_testing, key))

    except ModuleNotFoundError:
        pass
