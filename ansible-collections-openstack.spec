%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name ansible-pacemaker
%global commit ed36d82a0c60a841d2f30c61a50d60531481b2cc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git
%if 0%{?dlrn}
%define upstream_name ansible-collections-openstack.cloud
%else
%define upstream_name ansible-collections-openstack
%endif

Name:           ansible-collections-openstack
Version:        2.0.0
Release:        0.2%{?alphatag}%{?dist}
Summary:        Openstack Ansible collections
License:        GPLv3+
URL:            https://opendev.org/openstack/ansible-collections-openstack
Source0:        https://github.com/openstack/ansible-collections-openstack/archive/%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-pbr
BuildRequires:  python3-devel

Requires:       openstack-ansible-core
Requires:       python3-openstacksdk >= 0.13.0

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
* Wed Apr 19 2023 Alfredo Moralejo <amoralej@redhat.com> 2.0.0-0.2.ed36d82git
- Depend on openstack-ansible-core for compatibility with python 3.9

* Fri Nov 04 2022 Alfredo Moralejo <amoralej@redhat.com> - 2.0.0-0.1.ed36d82git
- Update to pre-2.0.0 commit (ed36d82a0c60a841d2f30c61a50d60531481b2cc)
