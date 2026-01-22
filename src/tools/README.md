Instead of building and maintaining custom or dummy pentesting tools (such as vuln_tools.py for vulnerability testing or code_tools.py for Python/shell execution), this project leverages an MCP-based pentesting server called HexStrike.

HexStrike provides access to 150+ production-ready cybersecurity tools designed for, Automated penetration testing, Vulnerability discovery, Bug bounty automation, Advanced security research.

For more details, please refer to the HexStrike repository:
https://github.com/0x4m4/hexstrike-ai


Tools such as file_tools.py, which provide a virtual file system, are already built into the DeepAgent library via LangChain, along with other native tools such as:

ls: List files in a directory (requires an absolute path).
read_file: Read a file using an absolute path, with support for pagination (offset, limit).
write_file: Create and write to a new file (absolute path required).
edit_file: Perform exact string replacements in existing files (requires a prior read).
glob: Find files matching a specified pattern (e.g., **/*.py).
grep: Search for text patterns across files (supports glob filters and multiple output modes).