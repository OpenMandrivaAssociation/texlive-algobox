%global tl_name algobox
%global tl_revision 67201

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Typeset Algobox programs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/algobox
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algobox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algobox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algobox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package can typeset Algobox programs almost exactly as
displayed when editing with Algobox itself, using an input syntax very
similar to the actual Algobox program text. It gives better results than
Algobox's own LaTeX export which does not look like the editor
rendition, produces standalone documents cumbersome to customize, and
has arbitrary and inconsistent differences between the input syntax and
the program text. This package depends upon the following other LaTeX
packages: expl3, TikZ, environ, xparse, and xcolor.

