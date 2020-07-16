from setuptools import setup, find_packages

setup_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %} ]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest>=3',{%- endif %} ]

setup(
    name='{{cookiecutter.package_name}}',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    version='1.0',
    description= '{{cookiecutter.application_short_description}}',
    include_package_data=True,
    url='https://gitlab.com/{{ cookiecutter.gitlab_username }}/{{ cookiecutter.package_name }}',
    zip_safe=False,
    packages=find_packages(include=['{{ cookiecutter.package_name }}', '{{ cookiecutter.package_name }}.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    install_requires=[
        'flask',
    ],
)
