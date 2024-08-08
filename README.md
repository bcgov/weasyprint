# WeasyPrint Container

## Usage

### Helm Chart Setup

#### In `Chart.yaml`:

```yaml
apiVersion: v2
name: main
description: A Helm chart
type: application
version: 0.1.0
appVersion: '0.1.0'
dependencies:
  - name: weasyprint
    version: '0.1.2'
    repository: https://bcgov.github.io/weasyprint
    condition: weasyprint.enabled
```

#### In `values.yaml`:

```yaml
weasyprint:
  enabled: true

  image:
    # Refer to https://github.com/bcgov/weasyprint/pkgs/container/weasyprint for available tags
    tag: 0000000000000000000000000000000000000000

  nameOverride: weasyprint
  fullnameOverride: weasyprint
```
