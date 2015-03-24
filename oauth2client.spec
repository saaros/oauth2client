Name:           python2-oauth2client
Version:        %{major_version}
Release:        %{minor_version}%{?dist}
Url:            http://github.com/ohmu/oauth2client
Summary:        Python 2 client library for OAuth 2.0
License:        ASL 2.0
Source0:        oauth2client-rpm-src.tar.gz
Requires:       python-httplib2, python-pyasn1, python-pyasn1-modules, python-six, python-rsa
BuildArch:      noarch

%description
Python 2 client library for accessing resources protected by OAuth 2.0.


%if %{?python3_sitelib:1}0
%package -n python3-oauth2client
Summary:        Python 3 client library for OAuth 2.0
Requires:       python3-httplib2, python3-pyasn1, python3-pyasn1-modules, python3-six, python3-rsa
BuildArch:      noarch

%description -n python3-oauth2client
Python 2 client library for accessing resources protected by OAuth 2.0.
%endif


%prep
%setup -q -n oauth2client


%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%if %{?python3_sitelib:1}0
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%endif


%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{python_sitelib}/*

%if %{?python3_sitelib:1}0
%files -n python3-oauth2client
%defattr(-,root,root,-)
%doc LICENSE README.md
%{python3_sitelib}/*
%endif


%changelog
* Tue Mar 24 2015 Oskari Saarenmaa <os@ohmu.fi> - 1.4.1-118
- Initial
