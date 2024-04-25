#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-evd
Version  : 2.3.7
Release  : 46
URL      : https://cran.r-project.org/src/contrib/evd_2.3-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/evd_2.3-7.tar.gz
Summary  : Functions for Extreme Value Distributions
Group    : Development/Tools
License  : GPL-3.0
Requires: R-evd-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
functions to univariate and multivariate parametric extreme
        value distributions, and provides fitting functions which
        calculate maximum likelihood estimates for univariate and
        bivariate maxima models, and for univariate and bivariate
        threshold models.

%package lib
Summary: lib components for the R-evd package.
Group: Libraries

%description lib
lib components for the R-evd package.


%prep
%setup -q -n evd
pushd ..
cp -a evd buildavx2
popd
pushd ..
cp -a evd buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713887166

%install
export SOURCE_DATE_EPOCH=1713887166
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/evd/CHANGES
/usr/lib64/R/library/evd/CITATION
/usr/lib64/R/library/evd/DESCRIPTION
/usr/lib64/R/library/evd/INDEX
/usr/lib64/R/library/evd/Meta/Rd.rds
/usr/lib64/R/library/evd/Meta/data.rds
/usr/lib64/R/library/evd/Meta/features.rds
/usr/lib64/R/library/evd/Meta/hsearch.rds
/usr/lib64/R/library/evd/Meta/links.rds
/usr/lib64/R/library/evd/Meta/nsInfo.rds
/usr/lib64/R/library/evd/Meta/package.rds
/usr/lib64/R/library/evd/Meta/vignette.rds
/usr/lib64/R/library/evd/NAMESPACE
/usr/lib64/R/library/evd/R/evd
/usr/lib64/R/library/evd/R/evd.rdb
/usr/lib64/R/library/evd/R/evd.rdx
/usr/lib64/R/library/evd/README
/usr/lib64/R/library/evd/data/Rdata.rdb
/usr/lib64/R/library/evd/data/Rdata.rds
/usr/lib64/R/library/evd/data/Rdata.rdx
/usr/lib64/R/library/evd/doc/Multivariate_Extremes.R
/usr/lib64/R/library/evd/doc/Multivariate_Extremes.Rnw
/usr/lib64/R/library/evd/doc/Multivariate_Extremes.pdf
/usr/lib64/R/library/evd/doc/guide22.pdf
/usr/lib64/R/library/evd/doc/guide22.txt
/usr/lib64/R/library/evd/doc/index.html
/usr/lib64/R/library/evd/help/AnIndex
/usr/lib64/R/library/evd/help/aliases.rds
/usr/lib64/R/library/evd/help/evd.rdb
/usr/lib64/R/library/evd/help/evd.rdx
/usr/lib64/R/library/evd/help/paths.rds
/usr/lib64/R/library/evd/html/00Index.html
/usr/lib64/R/library/evd/html/R.css

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/evd/libs/evd.so
/V4/usr/lib64/R/library/evd/libs/evd.so
/usr/lib64/R/library/evd/libs/evd.so
