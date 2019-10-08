let s:init_file_dir = ''
if has('mac')
  let s:init_file_dir = '.vim'
elseif has('win32') || has('win64')
  let s:init_file_dir = 'vimfiles'
endif

execute('source ~/' . s:init_file_dir . '/vimrc')
