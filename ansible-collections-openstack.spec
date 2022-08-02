%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global collection_namespace openstack
%global collection_name cloud

%{?dlrn: %global tarsources ansible-collections-openstack.cloud}
%{!?dlrn: %global tarsources ansible-collections-openstack}

Name:           ansible-collections-openstack
Version:        XXX
Release:        XXX
Summary:        Openstack Ansible collections
License:        GPLv3+
URL:            %{ansible_collection_url}
Source0:        https://github.com/openstack/%{name}/archive/%{upstream_version}.tar.gz#/%{collection_namespace}-%{collection_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  ansible-packaging
Requires:       python3-openstacksdk >= 0.13.0

%description
Openstack Ansible collections

%prep
%autosetup -n %{tarsources}-%{upstream_version}
sed -i -e 's/version:.*/version: %{version}/' galaxy.yml
rm -vr changelogs/ ci/ contrib/ tests/ ./galaxy.yml.in .zuul.yaml

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%doc README.md
%license COPYING
%{ansible_collection_files}

%changelog
