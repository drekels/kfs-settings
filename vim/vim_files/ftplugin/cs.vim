
" Automatically create block
nmap <C-a> o{<ESC>o}<ESC><UP>$o
imap <C-a> <ESC>o{<ESC>o}<ESC><UP>$o
nmap <C-\> iDebug.Log(string.Format("{0}", ));<ESC>^f"i<CR><BS><BS><ESC>$hhi<CR><BS><ESC>k$a
imap <C-\> Debug.Log(string.Format("{0}", ));<ESC>^f"i<CR><BS><BS><ESC>$hhi<CR><BS><ESC>k$a
