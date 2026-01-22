---
name: assessment-management
description: For tracking, managing, and prioritizing all activities and findings throughout the entire security assessment lifecycle.
---

# Assessment Management Skill

## When to Use This Skill

This is a continuous, overarching skill that should be active from the beginning to the end of the assessment. It is not for discovering vulnerabilities but for maintaining a centralized, organized record of the entire operation. It is best handled by a dedicated management subagent or the main supervisor agent.

## Primary Tools

- `msf_vulnerability_tracker`

## Workflow

1.  **Initialize Assessment**: Before any scanning begins, ensure the `msf_vulnerability_tracker` is ready to log findings for the new assessment.

2.  **Log Findings Continuously**: As subagents using other skills (like `web-vulnerability-scanning` and `post-exploitation`) report their findings, use `msf_vulnerability_tracker` with `action: "add"` to log each one. The log entry must include a detailed description, location (URL/parameter), severity, and any proof-of-concept code.

3.  **Prioritize Vulnerabilities**: Periodically, use `msf_vulnerability_tracker` to review all logged findings. Apply filters based on CVSS scores or vulnerability type to prioritize the most critical issues that require immediate attention or deeper investigation.

4.  **Update Finding Status**: As vulnerabilities are verified, exploited, or remediated, update their status within the `msf_vulnerability_tracker`. This ensures the assessment progress is accurately reflected at all times.