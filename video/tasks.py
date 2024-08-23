import subprocess


# def convert_video(source, resolution):
#     # Erstellen des neuen Dateinamens basierend auf der Auflösung
#     new_file_name = source[:-4] + f'_{resolution}.mp4'
#     cmd = [
#         'ffmpeg',
#         '-i', source, 
#         '-s', f'hd{resolution}',
#         '-c:v', 'libx264',
#         '-crf', '23',
#         '-c:a', 'aac',
#         '-strict', '-2',
#         new_file_name
#     ]
#     run = subprocess.run(cmd, capture_output=True)
    
#     # Rückgabe des Pfads der konvertierten Datei, falls erfolgreich
#     if run.returncode == 0:
#         return new_file_name
#     else:
#         # Bei Fehler None zurückgeben (kann durch Logging erweitert werden)
#         return None



# def convert720p(source, video_instance):
#     file_path = convert_video(source, '720')
#     if file_path:
#         video_instance.video_file_720p = file_path
#         video_instance.save(update_fields=['video_file_720p'])


# def convert480p(source, video_instance):
#     file_path = convert_video(source, '480')
#     if file_path:
#         video_instance.video_file_480p = file_path
#         video_instance.save(update_fields=['video_file_480p'])


# def convert1080p(source, video_instance):
#     file_path = convert_video(source, '1080')
#     if file_path:
#         video_instance.video_file_1080p = file_path
#         video_instance.save(update_fields=['video_file_1080p'])



def convert720p(source):      
    new_file_name = source[:-4] + '_720p.mp4'   
    cmd = [
        'ffmpeg',
        '-i', source, 
        '-s', 'hd720',
        '-c:v', 'libx264',
        '-crf', '23',
        '-c:a', 'aac',
        '-strict', '-2',
        new_file_name
    ] 
    run = subprocess.run(cmd, capture_output=True)
    
    
def convert480p(source):      
    new_file_name = source[:-4] + '_480p.mp4'   
    cmd = [
        'ffmpeg',
        '-i', source, 
        '-s', 'hd480',
        '-c:v', 'libx264',
        '-crf', '23',
        '-c:a', 'aac',
        '-strict', '-2',
        new_file_name
    ] 
    run = subprocess.run(cmd, capture_output=True)
    
    
def convert1080p(source):      
    new_file_name = source[:-4] + '_1080p.mp4'   
    cmd = [
        'ffmpeg',
        '-i', source, 
        '-s', 'hd1080',
        '-c:v', 'libx264',
        '-crf', '23',
        '-c:a', 'aac',
        '-strict', '-2',
        new_file_name
    ] 
    run = subprocess.run(cmd, capture_output=True)