%global tl_name hfutthesis
%global tl_revision 64025

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.4
Release:	%{tl_revision}.1
Summary:	LaTeX Thesis Template for Hefei University of Technology
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/hfutthesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hfutthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hfutthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This project is based on the HFUT_Thesis LaTeX template of Hefei
University of Technology compiled on the basis of ustctug/ustcthesis, in
accordance with the latest version of Hefei University of Technology
Graduate Dissertation Writing Specifications and Hefei University of
Technology Undergraduate Graduation Project (Thesis) Work Implementation
Rules.

