%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-collections-openstack
Version:        2.1.0
Release:        1%{?dist}
Summary:        Openstack Ansible collections
License:        GPLv3+
URL:            https://opendev.org/openstack/ansible-collections-openstack
Source0:        https://galaxy.ansible.com/download/openstack-cloud-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-pbr
BuildRequires:  python3-devel

Requires:       (ansible >= 2.8.0 or ansible-core >= 2.11)
Requires:       python3-openstacksdk >= 0.13.0

%description
Openstack Ansible collections

%prep
%autosetup -n ansible-collections-openstack.cloud-%{upstream_version}

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
* Thu Jul 13 2023 RDO <dev@lists.rdoproject.org> 2.1.0-1
- Update to 2.1.0

