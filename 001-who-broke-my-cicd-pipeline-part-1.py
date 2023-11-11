def compare_versions(line_a: str, line_b: str) -> None:
    mismatched_packages = dict()
    log_succeeded = line_a.split(" ")
    log_failed = line_b.split(" ")  
    
    pointer = 0
    while pointer < len(log_failed):
        if log_failed[pointer] != log_succeeded[pointer]:
            mismatched_packages[log_failed[pointer].split("-")[0]] = [log_failed[pointer].split("-")[1], log_succeeded[pointer].split("-")[1]]
            pointer += 1
        else:
            pointer += 1

    print(mismatched_packages)


def main():
    log_failed = (
        "Successfully installed Babel-2.13.0 Deprecated-1.2.14 GitPython-3.1.29 "
        "Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.2.3 acryl-datahub-0.10.4 agate-1.7.0 "
        "aiohttp-3.8.6 aiosignal-1.3.1 async-timeout-4.0.3 attrs-23.1.0 avro-1.10.2 "
        "avro-gen3-0.7.10 boto3-1.28.62 botocore-1.31.62 cached-property-1.5.2 "
        "certifi-2023.7.22 cffi-1.16.0 charset-normalizer-3.3.0 click-8.1.3 "
        "click-default-group-1.2.4 click-spinner-0.1.10 colorama-0.4.5 copier-7.0.1 "
        "data-pipelines-cli-0.26.0 dbt-core-1.5.4 dbt-extractor-0.4.1 dbt-postgres-1.5.4 "
        "docker-6.0.1 dunamai-1.19.0 entrypoints-0.4 expandvars-0.11.0 frozenlist-1.4.0 "
        "fsspec-2022.11.0 future-0.18.3 gitdb-4.0.10 hologram-0.0.16 humanfriendly-10.0 "
        "idna-3.4 ijson-3.2.3 isodate-0.6.1 iteration_utilities-0.11.0 "
        "jinja2-ansible-filters-1.3.2 jmespath-1.0.1 jsonref-1.1.0 jsonschema-4.19.1 "
        "jsonschema-specifications-2023.7.1 leather-0.3.4 logbook-1.5.3 mashumaro-3.6 "
        "minimal-snowplow-tracker-0.0.2 mixpanel-4.10.0 msgpack-1.0.7 multidict-6.0.4 "
        "mypy-extensions-1.0.0 networkx-2.8.8 packaging-21.3 parsedatetime-2.4 "
        "pathspec-0.11.2 plumbum-1.8.2 progressbar2-4.2.0 prompt_toolkit-3.0.36 "
        "protobuf-4.24.4 psutil-5.9.5 psycopg2-binary-2.9.9 pycparser-2.21 pydantic-1.10.13 "
        "pygments-2.16.1 pyparsing-3.1.1 python-dateutil-2.8.2 python-slugify-8.0.1 "
        "python-utils-3.8.1 pytimeparse-1.1.8 pytz-2023.3.post1 pyyaml-6.0 "
        "pyyaml-include-1.3.1 questionary-2.0.1 ratelimiter-1.2.0.post0 "
        "referencing-0.30.2 requests-2.31.0 requests-file-1.5.1 rpds-py-0.10.6 "
        "ruamel.yaml-0.17.35 ruamel.yaml.clib-0.2.8 s3transfer-0.7.0 six-1.16.0 "
        "smmap-5.0.1 sqlparse-0.4.4 tabulate-0.9.0 termcolor-2.3.0 text-unidecode-1.3 "
        "toml-0.10.2 types-PyYAML-6.0.12.2 typing-extensions-4.5.0 typing-inspect-0.9.0 "
        "tzlocal-5.1 urllib3-2.0.6 wcwidth-0.2.8 websocket-client-1.6.4 wrapt-1.15.0 yarl-1.9.2"
    )
    log_succeeded = (
        "Successfully installed Babel-2.13.0 Deprecated-1.2.14 GitPython-3.1.29 "
        "Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.2.3 acryl-datahub-0.10.4 agate-1.7.0 "
        "aiohttp-3.8.6 aiosignal-1.3.1 async-timeout-4.0.3 attrs-23.1.0 avro-1.10.2 "
        "avro-gen3-0.7.10 boto3-1.28.62 botocore-1.31.62 cached-property-1.5.2 "
        "certifi-2023.7.22 cffi-1.16.0 charset-normalizer-3.3.0 click-8.1.3 "
        "click-default-group-1.2.4 click-spinner-0.1.10 colorama-0.4.5 copier-7.0.1 "
        "data-pipelines-cli-0.26.0 dbt-core-1.5.4 dbt-extractor-0.4.1 dbt-postgres-1.5.4 "
        "docker-6.0.1 dunamai-1.19.0 entrypoints-0.4 expandvars-0.11.0 frozenlist-1.4.0 "
        "fsspec-2022.11.0 future-0.18.3 gitdb-4.0.10 hologram-0.0.16 humanfriendly-10.0 "
        "idna-3.4 ijson-3.2.3 isodate-0.6.1 iteration_utilities-0.11.0 "
        "jinja2-ansible-filters-1.3.2 jmespath-1.0.1 jsonref-1.1.0 jsonschema-4.19.1 "
        "jsonschema-specifications-2023.7.1 leather-0.3.4 logbook-1.5.3 mashumaro-3.6 "
        "minimal-snowplow-tracker-0.0.2 mixpanel-4.10.0 msgpack-1.0.7 multidict-6.0.4 "
        "mypy-extensions-1.0.0 networkx-2.8.8 packaging-21.3 parsedatetime-2.4 "
        "pathspec-0.11.2 plumbum-1.8.2 progressbar2-4.2.0 prompt_toolkit-3.0.36 "
        "protobuf-4.24.4 psutil-5.9.5 psycopg2-binary-2.9.9 pycparser-2.21 pydantic-1.10.13 "
        "pygments-2.16.1 pyparsing-3.1.1 python-dateutil-2.8.2 python-slugify-8.0.1 "
        "python-utils-3.8.1 pytimeparse-1.1.8 pytz-2023.3.post1 pyyaml-6.0 "
        "pyyaml-include-1.3.1 questionary-2.0.1 ratelimiter-1.2.0.post0 "
        "referencing-0.30.2 requests-2.31.0 requests-file-1.5.1 rpds-py-0.10.6 "
        "ruamel.yaml-0.17.35 ruamel.yaml.clib-0.2.8 s3transfer-0.7.0 six-1.16.0 "
        "smmap-5.0.1 sqlparse-0.4.4 tabulate-0.9.0 termcolor-2.3.0 text-unidecode-1.3 "
        "toml-0.10.2 types-PyYAML-6.0.12.2 typing-extensions-4.5.0 typing-inspect-0.9.0 "
        "tzlocal-5.1 urllib3-1.26.17 wcwidth-0.2.8 websocket-client-1.6.4 wrapt-1.15.0 yarl-1.9.2"
    )

    compare_versions(log_succeeded, log_failed)


if __name__ == '__main__':
    main()