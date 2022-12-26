Secret key is hard coded

Username: lance
Password: magical-hobby


Server is hosted on AWS EC2. [See notes.](https://docs.google.com/document/d/1Jg7w1vZw3HWMZ8RpLeIi2nxvI2HWu22r0MUVxUPdurE/edit#)

users:
- ubuntu (root)
- lance (hosts the site)

Wedding site:
- /home/lance/django-wedding-website

To upload new code:
1. In Windows Terminal, `ssh -i ".\.ssh\extreme_pem_aws_20220814.pem" lance@ec2-18-219-76-235.us-east-2.compute.amazonaws.com`
2. `cd django-wedding-website`
3. `git pull`
4. `source .venv/bin/activate`
5. `python manage.py collectstatic`
