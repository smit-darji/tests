docker run  -it -v tests:/home/glue_user/workspace/  -e DISABLE_SSL=true --rm -p 4042:4040 -p 18082:18080 --name glue_pytest amazon/aws-glue-libs:glue_libs_3.0.0_image_01 -c "python3 -m pytest"
