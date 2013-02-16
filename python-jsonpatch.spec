Name:           python-jsonpatch
Version:        0.12.0
Release:        1%{?dist}
Summary:        Applying JSON Patches in Python

License:        Modified BSD License
URL:            http://pypi.python.org/pypi/jsonpatch/0.12
Source0:        http://pypi.python.org/packages/source/j/jsonpatch/jsonpatch-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel


%description
Build self-validating python objects using JSON schemas

%prep
%setup -q -n jsonpatch-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.md
%{python_sitelib}/jsonpatch
%{python_sitelib}/jsonpatch-%{version}-py?.?.egg-info

%changelog
* Fri Feb 15 2013 Dan Prince - 0.12.0-1
- Initial package.
