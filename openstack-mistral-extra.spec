%{!?upstream_version: %global upstream_version %{version}}
%global upstream_name mistral-extra

%{?!_licensedir:%global license %%doc}

Name:           python-mistral-extra
Summary:        Python library of additional tools and examples for Mistral Workflow Service.
Version:        XXX
Release:        XXX
License:        ASL 2.0
URL:            https://github.com/openstack/mistral-extra

Source0:        https://tarballs.openstack.org/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires: python-oslo-log >= 3.11.0
Requires: python-babel >= 2.3.4
Requires: python-pbr >= 1.8

Provides:  mistral-extra = %{version}-%{release}
Obsoletes: mistral-extra < %{version}-%{release}

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -S git
rm -rf *.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

%description
Python library of additional tools and examples for Mistral Workflow Service.

%files
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{python2_sitelib}/mistral_extra
%exclude %{python2_sitelib}/mistral_extra/test*
%{_datadir}/%{name}
%{_datadir}/%{upstream_name}

%changelog

