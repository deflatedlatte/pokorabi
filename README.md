# pokorabi
Simple word learning app using LLMs

## Deployment
1. Build the image using Dockerfile.
2. Execute `docker run -d pokorabi-api`.

## Development
Pokorabi comes with a simple built-in web for development.

You can enable it by either:

- Setting environment variable `POKORABI_ENABLE_BUILTIN_WEBSITE` to `yes`
- Setting `website.enable_website` in `config.ini` to `yes`.

The environment variable has a higher precedence.
