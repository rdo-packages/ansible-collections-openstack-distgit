%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?dlrn}
%global upstream_name ansible-collections-openstack.cloud
%else
%global upstream_name ansible-collections-openstack
%endif

Name:           ansible-collections-openstack
Version:        1.5.0
Release:        1%{?dist}
Summary:        Openstack Ansible collections
License:        GPLv3+
URL:            https://opendev.org/openstack/ansible-collections-openstack
Source0:        https://github.com/openstack/%{name}/archive/%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python3-pbr
BuildRequires:  python3-devel

Requires:       ansible >= 2.8.0
Requires:       python3-openstacksdk >= 0.12.0

%description
Openstack Ansible collections

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -S git

%build
%py3_build

%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py3_install

%files

%doc README.md
%license COPYING
%{python3_sitelib}/ansible_collections_openstack.cloud-*.egg-info
%{_datadir}/ansible/collections/ansible_collections/openstack/cloud/

%changelog
* Thu Jun 24 2021 Sagi Shnaidman <sshnaidm@redhat.com> 1.5.0-1
- Update to 1.5.0

* Thu Apr 08 2021 Alfredo Moralejo <amoralej@redhat.com> 1.3.0-1
- Update to 1.3.0

# REMOVEME: error caused by commit https://opendev.org/openstack/ansible-collections-openstack/commit/f09cccdb9e6e211eb0dcb758a48bb2408d56e4c4
