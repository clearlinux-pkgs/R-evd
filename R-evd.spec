#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-evd
Version  : 2.3.3
Release  : 18
URL      : https://cran.r-project.org/src/contrib/evd_2.3-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/evd_2.3-3.tar.gz
Summary  : Functions for Extreme Value Distributions
Group    : Development/Tools
License  : GPL-3.0
Requires: R-evd-lib = %{version}-%{release}
BuildRequires : buildreq-R

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
%setup -q -c -n evd
cd %{_builddir}/evd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589532659

%install
export SOURCE_DATE_EPOCH=1589532659
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library evd
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library evd
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library evd
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc evd || :


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
/usr/lib64/R/library/evd/libs/evd.so
/usr/lib64/R/library/evd/libs/evd.so.avx2
/usr/lib64/R/library/evd/libs/evd.so.avx512
