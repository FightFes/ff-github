" gvimの設定
syntax on	            "シンタックスカラーリング
colorscheme eva01
"set background=dark
if has('nvim')  
  if exists('g:GuiLoaded')
    GuiTabline v:false
    if has('mac')
      GuiFont! Cica:h14
    elseif has('win64') || has('win32')
      GuiFont! Cica:h9
    endif
  endif
else
  if has('mac')
    set guifont=Cica:h14
    set antialias
  elseif has('win64') || has('win32')
    set guifont=Cica:h11
    set renderoptions=type:directx,renmode:5
  endif
  set guioptions-=T    "ツールバー非表示
  set guioptions-=m    "メニュー非表示
  "set guioptions-=r    "右スクロールバー非表示
  set guioptions-=R    
  set guioptions-=l    "左スクロールバー非表示
  set guioptions-=L    
  set guioptions-=e    "gvimでもテキストベースのタブを使用する
  winpos 424 217  " 表示位置
  set lines=73    " 縦幅
  set columns=272 " 横
endif
set ambiwidth=double
"autocmd FocusGained * set transparency=100
"autocmd FocusLost * set transparency=30

"eva01
hi Comment cterm=NONE gui=NONE
hi Visual cterm=NONE gui=NONE
"hi Search ctermfg=97  ctermbg=119 cterm=NONE guifg=#875FAF guibg=#87FF5F gui=NONE
"hi Search cterm=NONE guifg=#D0D0D0 guibg=#875FAF gui=NONE
hi Search cterm=NONE guifg=#FFFFFF guibg=#875FAF gui=NONE
hi IncSearch cterm=NONE gui=NONE
hi! NormalFloat cterm=NONE guifg=#FFFFFF guibg=#875FAF gui=NONE
" vimdiffの色設定
hi DiffAdd    gui=NONE guifg=#AF5FFF guibg=#87FF5F
hi DiffChange gui=NONE guifg=#AF5FFF guibg=#87FF5F
hi DiffDelete gui=NONE guifg=#87FF5F guibg=#D75F87
hi DiffText   gui=NONE guifg=#D7AF5F guibg=#87FF5F
