## GitHub Copilot Chat

- Extension Version: 0.30.0 (prod)
- VS Code: vscode/1.103.0
- OS: Linux
- Remote Name: codespaces

## Network

User Settings:
```json
  "github.copilot.advanced.debug.useElectronFetcher": true,
  "github.copilot.advanced.debug.useNodeFetcher": false,
  "github.copilot.advanced.debug.useNodeFetchFetcher": true
```

Connecting to https://api.github.com:
- DNS ipv4 Lookup: 140.82.113.6 (1 ms)
- DNS ipv6 Lookup: Error (13 ms): getaddrinfo ENOTFOUND api.github.com
- Proxy URL: None (270 ms)
- Electron fetch: Unavailable
- Node.js https: HTTP 200 (193 ms)
- Node.js fetch (configured): HTTP 200 (225 ms)

Connecting to https://api.individual.githubcopilot.com/_ping:
- DNS ipv4 Lookup: 140.82.113.21 (3 ms)
- DNS ipv6 Lookup: Error (4 ms): getaddrinfo ENOTFOUND api.individual.githubcopilot.com
- Proxy URL: None (342 ms)
- Electron fetch: Unavailable
- Node.js https: HTTP 200 (209 ms)
- Node.js fetch (configured): HTTP 200 (231 ms)

## Documentation

In corporate networks: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).