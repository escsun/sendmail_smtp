from utils import send_mail_smtp, file_to_text, current_date

# Default
subject = "This is example subject"
body = "This is example body"
# Custom functions
subject_with_date = "This is subject with current date {date}".format(date=current_date())
body_with_file = file_to_text("sample.txt")
# email to
email_to = "example_to@mail.com"


def main():
    # simple mail
    send_mail_smtp(subject, body, email_to)
    # with custom functions
    send_mail_smtp(subject_with_date, body_with_file, email_to)

if __name__ == "__main__":
    main()
