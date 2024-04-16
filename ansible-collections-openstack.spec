%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%{?dlrn: %global tarsources ansible-collections-openstack.cloud}
%{!?dlrn: %global tarsources ansible-collections-openstack}

Name:           ansible-collections-openstack
Version:        2.2.0
Release:        1%{?dist}
Summary:        Openstack Ansible collections
License:        GPLv3+
URL:            https://opendev.org/openstack/ansible-collections-openstack
Source0:        https://github.com/openstack/%{name}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
# (amoralej) We can remove this patch when we move to next release after 2.2.0
%if %{lua:print(rpm.vercmp(rpm.expand("%{version}"), '2.2.0'));} <= 0
Patch0:         0001-Disable-auto-discovery-for-setuptools.patch
%endif

BuildRequires:  git-core
BuildRequires:  python3-pbr
BuildRequires:  python3-devel

Requires:       openstack-ansible-core
Requires:       python3-openstacksdk >= 0.13.0

%description
Openstack Ansible collections

%prep
%autosetup -n %{tarsources}-%{upstream_version} -S git

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
* Tue Apr 16 2024 RDO <dev@lists.rdoproject.org> 2.2.0-1
- Update to 2.2.0

