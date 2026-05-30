# ROS 2 Workspace — Yahboom ROSMASTER X3

ROS 2 Jazzy + Gazebo Harmonic 기반 Yahboom ROSMASTER X3 메카넘 휠 AMR 시뮬레이션 워크스페이스.

## 환경

- ROS 2 Jazzy (Ubuntu Noble 24.04)
- Gazebo Harmonic (gz-sim 8)
- 물리 엔진: DART (`gz-physics-dartsim-plugin`)

---

## 새 컴퓨터 필수 설정

> [!warning] 새 컴퓨터 필수 작업
> `gz.transport13` Python 바인딩은 ROS 2 Jazzy / Gazebo Harmonic apt 패키지에 **포함되어 있지 않다.**
> 설치하지 않으면 `gz_pose_tf_publisher`가 Gazebo 포즈 구독에 실패하고, RViz에 `map` 프레임이 나타나지 않는다.

---

### 설치 절차

**Step 1.** gz-transport13 소스 클론

```bash
git clone --depth 1 --branch gz-transport13 https://github.com/gazebosim/gz-transport.git /tmp/gz-transport-src
```

**Step 2.** Python 바인딩 빌드

```bash
cmake -B /tmp/gz-transport-src/python/build -S /tmp/gz-transport-src/python -DCMAKE_BUILD_TYPE=Release
cmake --build /tmp/gz-transport-src/python/build --parallel $(nproc)
cmake --install /tmp/gz-transport-src/python/build --prefix /tmp/gz-transport-install
```

**Step 3.** user site-packages에 설치

```bash
SITE=$(python3 -c "import site; print(site.getusersitepackages())")
mkdir -p "$SITE/gz/transport13"
cp /tmp/gz-transport-install/lib/python/gz/transport13/_transport.cpython-*.so "$SITE/gz/transport13/"
cp /tmp/gz-transport-install/lib/python/gz/transport13/__init__.py "$SITE/gz/transport13/"
```

**Step 4.** gz.msgs10 경로를 ~/.bashrc에 추가

```bash
echo 'export PYTHONPATH="/opt/ros/jazzy/opt/gz_msgs_vendor/lib/python:$PYTHONPATH"' >> ~/.bashrc
source ~/.bashrc
```

**Step 5.** 정상 설치 확인

```bash
python3 -c "import gz.transport13; import gz.msgs10.pose_v_pb2; print('OK')"
```

---

## 빌드 및 실행

```bash
# 빌드
colcon build
source install/setup.bash

# 시뮬레이션 실행 (factory map)
bash src/yahboom_rosmaster/yahboom_rosmaster_bringup/scripts/rosmaster_x3_gazebo_2.sh
```
