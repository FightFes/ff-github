if exists('g:GuiLoaded')
  call GuiWindowMaximized(1)
  GuiTabline v:false
  GuiPopupmenu v:false
  " GuiLinespace 0
  if has('mac')
    GuiFont! Cica:h14
  elseif has('win64') || has('win32')
    GuiFont! Cica:h10
  endif

  nnoremap <silent> <C-6> <C-^>
endif
