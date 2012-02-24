# revision 25104
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-science
Epoch:		1
Version:	20120224
Release:	1
Summary:	Typesetting for natural and computer sciences
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-science.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-SIstyle
Requires:	texlive-SIunits
Requires:	texlive-alg
Requires:	texlive-algorithm2e
Requires:	texlive-algorithmicx
Requires:	texlive-algorithms
Requires:	texlive-biocon
Requires:	texlive-bpchem
Requires:	texlive-bytefield
Requires:	texlive-chemarrow
Requires:	texlive-chemcompounds
Requires:	texlive-chemcono
Requires:	texlive-chemexec
Requires:	texlive-chemmacros
Requires:	texlive-chemnum
Requires:	texlive-chemstyle
Requires:	texlive-clrscode
Requires:	texlive-complexity
Requires:	texlive-computational-complexity
Requires:	texlive-digiconfigs
Requires:	texlive-drawstack
Requires:	texlive-dyntree
Requires:	texlive-eltex
Requires:	texlive-engtlc
Requires:	texlive-fouridx
Requires:	texlive-functan
Requires:	texlive-galois
Requires:	texlive-gastex
Requires:	texlive-gene-logic
Requires:	texlive-gu
Requires:	texlive-hep
Requires:	texlive-hepnames
Requires:	texlive-hepparticles
Requires:	texlive-hepthesis
Requires:	texlive-hepunits
Requires:	texlive-karnaugh
Requires:	texlive-mhchem
Requires:	texlive-miller
Requires:	texlive-mychemistry
Requires:	texlive-nuc
Requires:	texlive-objectz
Requires:	texlive-physymb
Requires:	texlive-pseudocode
Requires:	texlive-sasnrdisplay
Requires:	texlive-sciposter
Requires:	texlive-sfg
Requires:	texlive-siunitx
Requires:	texlive-steinmetz
Requires:	texlive-struktex
Requires:	texlive-t-angles
Requires:	texlive-textopo
Requires:	texlive-ulqda
Requires:	texlive-unitsdef
Requires:	texlive-youngtab
Requires:	texlive-collection-latex

%description
Typesetting for natural and computer sciences.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install