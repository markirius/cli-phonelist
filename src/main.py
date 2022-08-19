#!/usr/bin/python3
import argparse

from phonebook import Contact


def create_contact():
    parse = argparse.ArgumentParser(
            prog='PHONEBOOK',
            description='Contact create'
        )
    parse.add_argument(
            '-n',
            '--name',
            type=str,
            help='inform contact name on this field',
            required=True
        )
    parse.add_argument(
            '-c',
            '--contact',
            type=str,
            help='inform the phone number on this field',
            required=True
        )
    parse.add_argument(
            '-e',
            '--email',
            type=str,
            help='inform contact e-mail on this field'
        )
    args = parse.parse_args()

    cont = Contact(name=args.name, contact=args.contact, email=args.email)
    cont.save()
    print('save by create contact method.')


if __name__ == '__main__':
    contacts = Contact.select().where(Contact.name.startswith('M'))
    for contact in contacts:
        print(f'{contact.name} | {contact.contact} | {contact.email}')
