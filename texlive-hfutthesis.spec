Name:		texlive-hfutthesis
Version:	64025
Release:	2
Summary:	LaTeX Thesis Template for Hefei University of Technology
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hfutthesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hfutthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hfutthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This project is based on the HFUT_Thesis LaTeX template of
Hefei University of Technology compiled on the basis of
ustctug/ustcthesis, in accordance with the latest version of
Hefei University of Technology Graduate Dissertation Writing
Specifications and Hefei University of Technology Undergraduate
Graduation Project (Thesis) Work Implementation Rules.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/hfutthesis
%doc %{_texmfdistdir}/doc/xelatex/hfutthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
