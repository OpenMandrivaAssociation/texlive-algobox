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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/algobox
%dir %{_datadir}/texmf-dist/source/latex/algobox
%dir %{_datadir}/texmf-dist/tex/latex/algobox
%doc %{_datadir}/texmf-dist/doc/latex/algobox/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/algobox/README.md
%doc %{_datadir}/texmf-dist/doc/latex/algobox/algobox.pdf
%doc %{_datadir}/texmf-dist/source/latex/algobox/algobox.dtx
%doc %{_datadir}/texmf-dist/source/latex/algobox/algobox.ins
%{_datadir}/texmf-dist/tex/latex/algobox/algobox.sty
