ext_info.py ~/Downloads/ | while read suf cnt sz; do hsz=$(numfmt --to=si "$sz"); echo "$suf $cnt $hsz"; done
