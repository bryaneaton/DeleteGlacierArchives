#!/usr/bin/env python3

import json, subprocess


if __name__ == '__main__':

    input_file_name = 'output.json'
    vault_name = 'QNAPVault'
    account_id = '947379795640'

    with open("/Users/b7e/amazon/output.json", "r") as write_file:
        data = json.load(write_file)

    archive_list = data['ArchiveList']

    count = 0
    filesLeft = len(archive_list)

    for archive in archive_list:
        count += 1
        filesLeft -= 1
        print(f"Deleting archive {archive['ArchiveId']} - files remaining: {filesLeft}")
        command = "aws glacier delete-archive --archive-id='" + archive['ArchiveId'] + "' --vault-name " + vault_name + " --account-id " + account_id
        subprocess.run(command, shell=True, check=True)









