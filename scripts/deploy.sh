#!/bin/sh
set -eu

phase=${1:?Expected deployment phase}
artifact=${2:?Expected immutable artifact path}

case "$phase" in
    test|production|smoke-test|smoke-production) ;;
    *) printf '%s\n' 'Unknown deployment phase; refusing execution.' >&2; exit 1 ;;
esac

test -f "$artifact" || { printf '%s\n' 'Release artifact is missing.' >&2; exit 1; }
printf '%s\n' "Adapter for $phase is not configured. Follow docs/deployment.md." >&2
exit 1