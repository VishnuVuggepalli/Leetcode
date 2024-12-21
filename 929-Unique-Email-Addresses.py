class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final_set =set()
        for email in emails:
            local_n , domain_n = email.split("@")
            local_n = local_n.split("+")[0]
            local_n = local_n.replace(".","")

            formatted_email = f"{local_n}@{domain_n}"

            final_set.add(formatted_email)

        return len(final_set)
        #     s= ""
        #     letter = 0
        #     while letter < len(email):
        #         if email[letter] == "@":
        #             s += email[letter:len(email)]
        #             break
        #         elif email[letter] == '+':
        #             while email[letter] != '@':
        #                 letter += 1
        #         elif email[letter] == ".":
        #             letter += 1
        #             continue
        #         else:
        #             s += email[letter]
        #             letter += 1
        #     final_set.add(s)
        # return len(final_set)