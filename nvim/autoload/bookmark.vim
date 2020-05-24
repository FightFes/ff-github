" ============================================================================
" FILE: bookmark.vim
" AUTHOR: <kinntai at gmail.com>
" License: MIT license
" ============================================================================

let s:cache_directory_path = "~/.cache/denite-bookmark"
let s:cache_file_name = "bookmark.json"
let s:default_group_name = "default"

function! bookmark#set_cache_directory_path(path)
  let s:cache_directory_path = a:path
endfunction

function! bookmark#get_cache_directory_path()
  return fnamemodify(s:cache_directory_path, ":p")
endfunction

function! bookmark#get_cache_file_path()
  return bookmark#get_cache_directory_path() . "/" . s:cache_file_name
endfunction

function! bookmark#set_default_group(group)
  let s:default_group_name = a:group
endfunction

function! bookmark#get_default_group()
  return s:default_group_name
endfunction
