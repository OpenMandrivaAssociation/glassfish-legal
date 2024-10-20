%{?_javapackages_macros:%_javapackages_macros}
Name:          glassfish-legal
Version:       1.1
Release:       3.0%{?dist}
Summary:       Legal License for glassfish code
License:       CDDL or GPLv2 with exceptions
URL:           https://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/ glassfish-legal-1.1
# tar czf glassfish-legal-1.1-src-svn.tar.gz glassfish-legal-1.1
Source0:       %{name}-%{version}-src-svn.tar.gz

BuildRequires: java-devel

BuildRequires: glassfish-master-pom
BuildRequires: maven-local
BuildRequires: maven-remote-resources-plugin

Requires:      glassfish-master-pom
BuildArch:     noarch

%description
An archive which contains license files for glassfish code.

%prep
%setup -q -n %{name}-%{version}

sed -i 's/\r//' src/main/resources/META-INF/LICENSE.txt
cp -p src/main/resources/META-INF/LICENSE.txt .

%build

%mvn_file :legal %{name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 gil cattaneo <puntogil@libero.it> 1.1-2
- switch to XMvn
- minor changes to adapt to current guideline

* Wed Jan 16 2013 gil cattaneo <puntogil@libero.it> 1.1-1
- initial rpm