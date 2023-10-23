from main import cv_version
import cv2

def test_add():
    assert "4.8.1.78" in cv_version(cv2.version.VERSION)