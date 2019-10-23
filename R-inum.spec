#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-inum
Version  : 1.0.1
Release  : 24
URL      : https://cran.r-project.org/src/contrib/inum_1.0-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/inum_1.0-1.tar.gz
Summary  : Interval and Enum-Type Representation of Vectors
Group    : Development/Tools
License  : GPL-2.0
Requires: R-libcoin
BuildRequires : R-libcoin
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
of intervals, including a method of coercing variables in data frames.

%prep
%setup -q -c -n inum

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571847790

%install
export SOURCE_DATE_EPOCH=1571847790
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library inum
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library inum
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library inum
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc inum || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/inum/DESCRIPTION
/usr/lib64/R/library/inum/INDEX
/usr/lib64/R/library/inum/Meta/Rd.rds
/usr/lib64/R/library/inum/Meta/features.rds
/usr/lib64/R/library/inum/Meta/hsearch.rds
/usr/lib64/R/library/inum/Meta/links.rds
/usr/lib64/R/library/inum/Meta/nsInfo.rds
/usr/lib64/R/library/inum/Meta/package.rds
/usr/lib64/R/library/inum/NAMESPACE
/usr/lib64/R/library/inum/NEWS.Rd
/usr/lib64/R/library/inum/R/inum
/usr/lib64/R/library/inum/R/inum.rdb
/usr/lib64/R/library/inum/R/inum.rdx
/usr/lib64/R/library/inum/help/AnIndex
/usr/lib64/R/library/inum/help/aliases.rds
/usr/lib64/R/library/inum/help/inum.rdb
/usr/lib64/R/library/inum/help/inum.rdx
/usr/lib64/R/library/inum/help/paths.rds
/usr/lib64/R/library/inum/html/00Index.html
/usr/lib64/R/library/inum/html/R.css
/usr/lib64/R/library/inum/tests/bugfixes.R
/usr/lib64/R/library/inum/tests/bugfixes.Rout.save
/usr/lib64/R/library/inum/tests/regtest.R
/usr/lib64/R/library/inum/tests/regtest.Rout.save
