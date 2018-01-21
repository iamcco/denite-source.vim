"===============================================================================
"File: source.vim
"Maintainer: iamcco <ooiss@qq.com>
"Github: http://github.com/iamcco <年糕小豆汤>
"Licence: Vim Licence
"Version: 0.0.1
"===============================================================================

scriptencoding utf-8

" get denite source name list
function! source#get_source_list() abort
    let l:res = filter(
                \ map(
                \   globpath(
                \       &runtimepath,
                \       'rplugin/python3/denite/source/*.py',
                \       1,
                \       1,
                \   ),
                \ 'fnamemodify(v:val, ":t:r")'
                \ ),
                \ 'v:val !=# "base" && v:val !=# "__init__"'
                \)
    return l:res
endfunction
