# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif

%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?dlrn}
%define upstream_name ansible-collections-openstack.cloud
%else
%define upstream_name ansible-collections-openstack
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
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr

Requires:       ansible >= 2.8.0
Requires:       python%{pyver}-openstacksdk >= 0.12.0

%description
Openstack Ansible collections

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -S git

%build
%{pyver_build}

%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{pyver_install}

%files

%doc README.md
%license COPYING
%{pyver_sitelib}/ansible_collections_openstack.cloud-*.egg-info
%{_datadir}/ansible/collections/ansible_collections/openstack/cloud/

%changelog
* Thu Jun 24 2021 Sagi Shnaidman <sshnaidm@redhat.com> 1.5.0-1
- Update to 1.5.0

* Thu Apr 08 2021 Alfredo Moralejo <amoralej@redhat.com> 1.3.0-1
- Update to 1.3.0

# REMOVEME: error caused by commit https://opendev.org/openstack/ansible-collections-openstack/commit/27e113780f3ade8a0f387838a3efd3ee5327314d
