Name:		texlive-algobox
Version:	67201
Release:	1
Summary:	Typeset Algobox programs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/algobox
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algobox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algobox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algobox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package can typeset Algobox programs almost exactly
as displayed when editing with Algobox itself, using an input
syntax very similar to the actual Algobox program text. It
gives better results than Algobox's own LaTeX export which does
not look like the editor rendition, produces standalone
documents cumbersome to customize, and has arbitrary and
inconsistent differences between the input syntax and the
program text. This package depends upon the following other
LaTeX packages: expl3, TikZ, environ, xparse, and xcolor.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/algobox
%{_texmfdistdir}/tex/latex/algobox
%doc %{_texmfdistdir}/doc/latex/algobox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
