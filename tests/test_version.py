import pytest

from newversion.version import Version, VersionError


class TestVersion:
    def test_parse(self):
        assert Version.zero().dumps() == "0.0.0"
        assert Version("1.2.3").major == 1
        assert Version("1.2.3").minor == 2
        assert Version("1.2.3").micro == 3
        assert Version("1.2.3").pre == None
        assert Version("1.2.3rc4").pre == ("rc", 4)
        assert Version("1.2.3.alpha4").pre == ("a", 4)
        assert Version("1.2.3.alpha").pre == ("a", 0)
        assert Version("1.2.3-rc4").pre == ("rc", 4)
        assert Version("1.2.3-dev5").is_devrelease
        assert Version("1.2.3").is_stable
        assert not Version("1.2.3").is_devrelease
        assert Version("1.2.3.post3").is_stable
        assert Version("1.2.3.post3").is_postrelease

        with pytest.raises(VersionError):
            Version("invalid")

    def test_bump_major(self):
        assert Version("1.2.3").bump_major().dumps() == "2.0.0"
        assert Version("1.2.3rc4").bump_major(2).dumps() == "3.0.0"
        assert Version("2.0.0").bump_major().dumps() == "3.0.0"
        assert Version("2.0.0rc4").bump_major().dumps() == "2.0.0"
        assert Version("2.1.0rc4").bump_major().dumps() == "3.0.0"
        assert Version("2.1.0rc4").bump_major(2).dumps() == "4.0.0"

    def test_bump_minor(self):
        assert Version("1.2.3").bump_minor().dumps() == "1.3.0"
        assert Version("1.2.3rc4").bump_minor(2).dumps() == "1.4.0"
        assert Version("1.2.3rc4").bump_minor(0).dumps() == "1.2.0"
        assert Version("1.3.0rc4").bump_minor().dumps() == "1.3.0"
        assert Version("1.3.0rc4").bump_minor(2).dumps() == "1.4.0"
        assert Version("1").bump_minor().dumps() == "1.1.0"

    def test_bump_micro(self):
        assert Version("1.2.3").bump_micro().dumps() == "1.2.4"
        assert Version("1.2.3rc4").bump_micro().dumps() == "1.2.3"
        assert Version("1.2.3rc4").bump_micro(2).dumps() == "1.2.4"
        assert Version("1.2.3rc4").bump_micro(0).dumps() == "1.2.2"
        assert Version("1").bump_micro().dumps() == "1.0.1"
        assert Version("1.2").bump_micro().dumps() == "1.2.1"

    def test_bump_prerelease(self):
        assert Version("1.2.3").bump_prerelease().dumps() == "1.2.4rc1"
        assert Version("1.2.3alpha").bump_prerelease().dumps() == "1.2.3a2"
        assert Version("1.2.3rc4").bump_prerelease(2).dumps() == "1.2.3rc6"
        assert Version("1.2.3rc4").bump_prerelease(2, "alpha").dumps() == "1.2.4a2"
        assert Version("1.2.3").bump_prerelease(2, "alpha").dumps() == "1.2.4a2"
        assert Version("1.2.3").bump_prerelease(2, "alpha", "major").dumps() == "2.0.0a2"
        assert Version("1.2.3a3").bump_prerelease(2, "alpha", "major").dumps() == "1.2.3a5"
        assert Version("1.2.3a3").bump_prerelease(2, "rc", "major").dumps() == "1.2.3rc2"

    def test_bump_postrelease(self):
        assert Version("1.2.3").bump_postrelease().dumps() == "1.2.3.post1"
        assert Version("1.2.3alpha").bump_postrelease().dumps() == "1.2.3.post1"
        assert Version("1.2.3.post4").bump_postrelease(2).dumps() == "1.2.3.post6"
        assert Version("1.2.3.post").bump_postrelease().dumps() == "1.2.3.post2"
        assert Version("1.2.3").bump_postrelease(2).dumps() == "1.2.3.post2"

    def test_replace(self):
        assert Version("1.2.3").replace(dev=45).dumps() == "1.2.3.dev45"
        assert Version("1.2.3.dev14").replace(dev=36).dumps() == "1.2.3.dev36"
        assert Version("1.2.3-dev14").replace(dev=45).dumps() == "1.2.3.dev45"
        assert Version("1.2.3rc3").replace(dev=45).dumps() == "1.2.3rc3.dev45"
        assert Version("1.2.3rc3").replace(major=3).dumps() == "3.2.3rc3"
        assert Version("1.2.3rc3").replace(local="test-1").dumps() == "1.2.3rc3+test.1"

    def test_get_stable(self):
        assert Version("1.2.3").get_stable().dumps() == "1.2.3"
        assert Version("2.1.0a2").get_stable().dumps() == "2.1.0"
        assert Version("1.2.5.post3").get_stable().dumps() == "1.2.5"

    def test_comparison(self):
        assert Version("1.2.32") > Version("1.2.5")
        assert Version("1.2.3") > Version("1.2.3.rc3")
        assert Version("1.2.3.rc3") > Version("1.2.3.rc2")
        assert Version("1.2.3rc3") == Version("1.2.3.rc3")
        assert Version("1.2.3alpha3") == Version("1.2.3a3")
        assert Version("1.2.3.rc3") < Version("1.2.3.rc4")
        assert Version("1.2.3.rc3") < Version("1.2.3")
        assert Version("1.2.3.dev3") < Version("1.2.3a1")
        assert Version("1.2.3.post3") > Version("1.2.3")
