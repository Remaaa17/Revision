from typing import Iterable, Set

def collect_account_ids_from_arns(arns: Iterable[str]) -> Set[str]:
"""Given several ARNs in the form

arn:partition: service:region:account-id:resource-id

Collect the unique account IDs found on those strings, and return them."""

collected_account_ids = set()
for arn in arns:
 matched = re.match(ARN_REGEX, arn)
 if matched is not None:
   account_id = matched.groupdict()["account_id"]
   collected_account_ids.add(account_id)

return collected_account_ids

def collect_account_ids_from_arns(arns):
 matched_arns = filter(None, (re.match(ARN_REGEX, arn) for arn in arns))
    return {m.groupdict()["account_id"] for m in matched_arns}