————————————
Description
————————————

shot_detect.py performs shot detection and segments an input video into its constituent shots. The python script uses the command line tool ffmpeg for keyframe detection.

INPUT: the movie file ‘input.avi’
OUTPUT: shot timestamps (text file) and separate avi files for each shot

Keep this script and the input video (input.avi) in the same folder to perform the shot-detection and segmentation. Tune the threshold (I found 0.3 produces decent result) to achieve desired result.

—————
Note
—————
1) Make sure you have enough space in the drive, since the video is uncompressed before partitioning for precision. 
2) Change the ffmpeg codecs to transcode the video/audio.
3) I used only integer part (in sec) of the time stamps for simplicity.

_____
Notice
______
This code is written by Tanaya Guha and CheWei Huang, Signal Analysis and Interpretation Lab, Electrical Engineering, University of Southern California, Los Angeles, USA. 

March 07, 2014

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

Neither the name of the University of southern California nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.







