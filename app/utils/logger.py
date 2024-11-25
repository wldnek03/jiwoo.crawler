import logging

def setup_logger():
    logger = logging.getLogger('job_portal')
    logger.setLevel(logging.DEBUG)

    # 콘솔 출력 핸들러 추가
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 포맷 설정
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    
    return logger