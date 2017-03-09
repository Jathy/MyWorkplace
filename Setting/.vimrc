"-------------------------------vim base setting------------------------------

syntax on	"highlight
set wrap	"auto switch line
set number	"display line number

set incsearch 	"display the result when searching
set hlsearch	"highlight the keyworld when searching

set laststatus=2

set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab

set smartindent "auto indent when starting new line
set smarttab	"auto tab

"set cursorline
"set cursorcolumn

"hide scrollbar
set guioptions-=r
set guioptions-=L
set guioptions-=b

"Enable folding
set foldmethod=indent
set foldlevel=99
"Enable folding with the spacebar
nnoremap <space> za


"split setting
set splitbelow
set splitright
"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-L> <C-W><C-L>

"---------------------------------------------------------------------------












"-------- VundleVim Plugin Setting---------

"vimairline
"let g:airline#extensions#tabline#enabled = 1
let g:airline_theme='luna'


"nerdTree
"F2开启和关闭树"
map <F2> :NERDTreeToggle<CR>
let NERDTreeChDirMode=1
""显示书签"
let NERDTreeShowBookmarks=1
"设置忽略文件类型"
let NERDTreeIgnore=['\~$', '\.pyc$', '\.swp$']
""窗口大小"
let NERDTreeWinSize=25


"simpylFold
let g:SimpylFold_docstring_preview = 1

"缩进指示线"
let g:indentLine_char='┆'
let g:indentLine_enabled = 1

""autopep8设置"
let g:autopep8_disable_show_diff=1


"------------------------------------------



"------------------------------VundleVim------------------------------------
set nocompatible              " be iMproved, required
filetype off                  " required
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

"----Your Plugin------"
" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
"Plugin 'tpope/vim-fugitive'"
" plugin from http://vim-scripts.org/vim/scripts.html
"Plugin 'L9'"
" Git plugin not hosted on GitHub
"Plugin 'git://git.wincent.com/command-t.git'"
" git repos on your local machine (i.e. when working on your own plugin)
"Plugin 'file:///home/gmarik/path/to/plugin'"
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
"Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}"
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
"Plugin 'ascenator/L9', {'name': 'newL9'}"
Plugin 'Valloric/YouCompleteMe'
Plugin 'Lokaltog/vim-powerline'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'scrooloose/nerdtree'
Plugin 'Yggdroot/indentLine'
Plugin 'jiangmiao/auto-pairs'
Plugin 'tell-k/vim-autopep8'
Plugin 'scrooloose/nerdcommenter'
Plugin 'tmhedberg/SimpylFold'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
" --------------------------------------------------------------------------
