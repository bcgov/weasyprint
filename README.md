# WeasyPrint Container

This repository includes an API server and a Helm chart, offering endpoints for generating PDFs from HTML data with [WeasyPrint](https://github.com/Kozea/WeasyPrint).

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
    # Refer to https://github.com/bcgov/weasyprint/blob/gh-pages/index.yaml for available versions
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

### Running WeasyPrint Locally

To run WeasyPrint, a tool for creating PDF documents, in your local development environment, use the following command:

```sh
docker run -p 8080:8080 --pull always ghcr.io/bcgov/weasyprint:latest
```

This will start WeasyPrint on `http://localhost:8080`.

# API Documentation

This API provides a set of endpoints for basic status checks and PDF generation.

## Endpoints

### 1. Home Endpoint

- **URL**: `/`
- **Method**: `GET`
- **Description**: This endpoint checks the status of the API. It returns a simple JSON response indicating that the API is running.

- **Response**:
  - **Status**: `200 OK`
  - **Body**:
    ```json
    {
      "status": true
    }
    ```

### 2. Generate PDF Endpoint

- **URL**: `/pdf`
- **Method**: `POST`
- **Description**: This endpoint generates a PDF from the provided HTML and CSS. The generated PDF is returned as a downloadable file.

- **Request**:

  - **Content-Type**: `application/json`
  - **Body Parameters**:

    - `html` (string, required): The HTML content to be converted into a PDF.
    - `css` (string, optional): The CSS styles to apply to the HTML content. Defaults to an empty string.
    - `filename` (string, optional): The name of the generated PDF file. Defaults to `"download.pdf"`.

  - **Example**:
    ```json
    {
      "html": "<h1>Hello, World!</h1>",
      "css": "h1 { color: red; }",
      "filename": "hello.pdf"
    }
    ```

- **Response**:

  - **Status**: `200 OK`
  - **Headers**:
    - `Content-Disposition`: Contains the attachment details and filename.
  - **Body**: The generated PDF file as binary content.

  - **Example**:
    - **Headers**:
      ```
      Content-Disposition: attachment; filename='hello.pdf'
      ```
    - **Body**: The PDF file content.

## Default Fonts

### BC Sans Typeface (BCSans)

BC Sans (2.0) is an open-source, evolving typeface designed to enhance the readability and effectiveness of digital services in government. The fonts can be accessed at: [BC Sans Typeface](https://www2.gov.bc.ca/gov/content/governments/services-for-government/policies-procedures/bc-visual-identity/bc-sans).
